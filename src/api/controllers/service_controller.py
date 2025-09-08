from flask import Blueprint, request, jsonify

bp = Blueprint("service", __name__, url_prefix="/services")

# In-memory database giả lập
services = [
    {"id": 1, "name": "Spa Package", "price": 500000, "description": "Gói spa thư giãn"},
    {"id": 2, "name": "Airport Pickup", "price": 300000, "description": "Đưa đón sân bay"},
]

# Lấy danh sách tất cả dịch vụ
@bp.route("/", methods=["GET"])
def list_services():
    return jsonify(services), 200

# Lấy chi tiết dịch vụ theo ID
@bp.route("/<int:service_id>", methods=["GET"])
def get_service(service_id):
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service), 200

# Thêm dịch vụ mới
@bp.route("/", methods=["POST"])
def create_service():
    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_id = max([s["id"] for s in services], default=0) + 1
    new_service = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"],
        "description": data.get("description", "")
    }
    services.append(new_service)
    return jsonify(new_service), 201

# Cập nhật dịch vụ
@bp.route("/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    
    data = request.json
    service["name"] = data.get("name", service["name"])
    service["price"] = data.get("price", service["price"])
    service["description"] = data.get("description", service["description"])
    return jsonify(service), 200

# Xóa dịch vụ
@bp.route("/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    global services
    services = [s for s in services if s["id"] != service_id]
    return jsonify({"message": "Service deleted"}), 200
