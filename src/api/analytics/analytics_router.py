from flask import Blueprint, jsonify

# Tạo Blueprint cho analytics
analytics_bp = Blueprint("analytics", __name__, url_prefix="/api/admin/analytics")

@analytics_bp.route("/revenue", methods=["GET"])
def get_revenue_report():
    # Mock data doanh thu
    data = {
        "labels": ["Tháng 1", "Tháng 2", "Tháng 3"],
        "data": [12000000, 18000000, 15000000]
    }
    return jsonify(data)

@analytics_bp.route("/pod-usage", methods=["GET"])
def get_pod_usage():
    # Mock data usage
    data = {
        "labels": ["POD1", "POD2", "POD3"],
        "data": [80, 65, 90]
    }
    return jsonify(data)

@analytics_bp.route("/customers", methods=["GET"])
def get_customers_report():
    # Mock data khách hàng
    data = {
        "topServices": ["Gói A", "Gói B", "Gói C"],
        "frequency": [120, 95, 80]
    }
    return jsonify(data)