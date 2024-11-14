from psql.models import Email, Device, Location, ExplosiveSentence

def convert_json_to_email_model(email_json) -> Email:
    return Email(
        email_address = email_json['email'],
        username = email_json['username'],
        ip_address = email_json['ip_address'],
        email_date = email_json['created_at'],
        device = Device(
            device_id = email_json['device_info']['device_id'],
            os = email_json['device_info']['os'],
            browser = email_json['device_info']['browser']
        ),
        location = Location(
            lat = email_json['location']['latitude'],
            lon = email_json['location']['longitude'],
            city = email_json['location']['city'],
            country = email_json['location']['country']
        ),
        explosive_sentences = [ExplosiveSentence(sentence = sentence) for sentence in email_json['sentences']],
    )
