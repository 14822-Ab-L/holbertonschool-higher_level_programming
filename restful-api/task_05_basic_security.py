#!/usr/bin/python3
"""API security and authentication using Flask."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

# Set up authentication managers
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "your-secret-key"

jwt = JWTManager(app)

# Custom JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle requests with missing JWT tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT tokens."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked JWT tokens."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle requests requiring a fresh JWT token."""
    return jsonify({"error": "Fresh token required"}), 401


# Store users in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Verify Basic Authentication credentials
@auth.verify_password
def verify_password(username, password):
    """Verify a username and password."""

    if username in users:
        user = users[username]

        if check_password_hash(user["password"], password):
            return username

    return None


# Basic Authentication protected route
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message if Basic Authentication succeeds."""
    return "Basic Auth: Access Granted"


# JWT login route
@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT token."""

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users[username]

    if not isinstance(password, str) or not check_password_hash(
        user["password"], password
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify({"access_token": access_token}), 200


# JWT protected route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message if JWT authentication succeeds."""
    return "JWT Auth: Access Granted"


# Admin-only route
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Allow access only to administrators."""

    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()

#!/usr/bin/python3
"""API security and authentication using Flask."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

# Set up authentication managers
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "your-secret-key"

jwt = JWTManager(app)

# Custom JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle requests with missing JWT tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT tokens."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked JWT tokens."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle requests requiring a fresh JWT token."""
    return jsonify({"error": "Fresh token required"}), 401


# Store users in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Verify Basic Authentication credentials
@auth.verify_password
def verify_password(username, password):
    """Verify a username and password."""

    if username in users:
        user = users[username]

        if check_password_hash(user["password"], password):
            return username

    return None


# Basic Authentication protected route
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message if Basic Authentication succeeds."""
    return "Basic Auth: Access Granted"


# JWT login route
@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT token."""

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users[username]

    if not isinstance(password, str) or not check_password_hash(
        user["password"], password
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify({"access_token": access_token}), 200


# JWT protected route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message if JWT authentication succeeds."""
    return "JWT Auth: Access Granted"


# Admin-only route
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Allow access only to administrators."""

    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
