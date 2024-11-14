from psql.models import Email, ExplosiveSentence, HostageSentence, Device, Location
from dictalchemy.utils import asdict

def email_model_to_json(email: Email):
    return {
        'email info': asdict(email),
        'device': asdict(email.device),
        'location': asdict(email.location),
        'sentences': ([sentence.sentence for sentence in email.explosive_sentences] +
                      [sentence.sentence for sentence in email.hostage_sentences])
    }