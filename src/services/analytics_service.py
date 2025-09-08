def get_revenue_report():
    # Giả lập dữ liệu. Sau này sẽ thay bằng truy vấn DB
    return {
        "total_revenue": 52000000,
        "by_service": [
            {"service": "Gói ngày", "revenue": 20000000},
            {"service": "Gói tuần", "revenue": 15000000},
            {"service": "Gói tháng", "revenue": 17000000}
        ]
    }

def get_pod_usage_report():
    # Giả lập dữ liệu. Sau này sẽ thay bằng truy vấn DB
    return {
        "total_pods": 100,
        "used_pods": 72,
        "usage_rate": "72%"
    }

def get_revenue_report():
    # Dữ liệu mẫu – sau này sẽ truy vấn từ database thật
    return {
        "total_revenue": 15000000,
        "by_package": {
            "Basic": 5000000,
            "Premium": 7000000,
            "VIP": 3000000
        }
    }

def get_pod_usage_report():
    # Dữ liệu mẫu – thay bằng dữ liệu thực tế từ DB
    total_pods = 20
    used_pods = 16
    usage_rate = round((used_pods / total_pods) * 100, 2)  # 80.0%

    return {
        "total_pods": total_pods,
        "used_pods": used_pods,
        "usage_rate_percent": f"{usage_rate}%"  # Ví dụ: "80.0%"
    }