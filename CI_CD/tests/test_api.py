import json


def test_app_import_and_health():
    from CI_CD.app import app
    client = app.test_client()  # Flask instance

    resp = client.get("/health")
    assert resp.status_code == 200


def test_predict_endpoint():
    from CI_CD.app import app

    client = app.test_client()

    payload = {
        "features": {
            "Pclass": 3,
            "Sex": "male",
            "Age": 22,
            "SibSp": 1,
            "Parch": 0,
            "Fare": 7.25,
            "Embarked": "S",
        }
    }

    resp = client.post(
        "/predict",
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data["predictions"], list)


