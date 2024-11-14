import psql.repository.email_repository as email_repos
import email_endpoint.app.utils.convert_utils as utils


def get_email_info_by_email_address(email_address):
    email_list = email_repos.get_emails_by_email_address(email_address)
    return [utils.email_model_to_json(email) for email in email_list]