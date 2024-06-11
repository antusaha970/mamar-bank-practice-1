from django.urls import path
from .views import DepositMoneyView, WithdrawalMoneyView, LoanMoneyView, LoanListView, TransactionReportView, PayLoanView, SendMoneyView

urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name="deposit_money"),
    path('withdraw/', WithdrawalMoneyView.as_view(), name="withdrawal_money"),
    path('report/', TransactionReportView.as_view(), name="transaction_report"),
    path('send_money/', SendMoneyView.as_view(), name="send_money"),
    path('loan_request/', LoanMoneyView.as_view(), name="loan_request"),
    path('loans/', LoanListView.as_view(), name="loan_list"),
    path('loan/<int:loan_id>/', PayLoanView.as_view(), name="pay_loan"),
]
