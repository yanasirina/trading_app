from fastapi import APIRouter, Depends

from auth.router import current_user
from sender.tasks import send_email_report_dashboard


router = APIRouter(
    prefix="/sender",
    tags=["Sender"]
)


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.email)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
