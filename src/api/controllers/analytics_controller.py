from flask import Blueprint, jsonify
from src.services.analytics_service import get_revenue_report, get_pod_usage_report
from src.api.responses import success_response

bp = Blueprint('analytics', __name__)

@bp.route('/admin/revenue', methods=['GET'])
def revenue_report():
    """
    Lấy báo cáo doanh thu tổng thể và theo gói dịch vụ.
    """
    data = get_revenue_report()
    return success_response(data)


@bp.route('/admin/pod-usage', methods=['GET'])
def pod_usage_report():
    """
    Lấy báo cáo hiệu suất sử dụng POD (tỷ lệ lấp đầy).
    """
    data = get_pod_usage_report()
    return success_response(data)