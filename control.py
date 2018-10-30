class ControlAbility(object):
    def add_method(self, name, http_method, payload, body):
        control_dict = self.setdefault('control', {})
        control_dict[name] = {
            "endpoint": '{} domain/resource'.format(http_method),
            "payload": [],
            "response": {
                "status": True,
                "body": []
            }
        }

        for _id, value in payload:
            control_dict[name]['payload'].append(
                {
                    "id": _id,
                    "value": value
                }
            )

        for _id, value in body:
            control_dict[name]['response']['body'].append(
                {
                    "id": _id,
                    "value": value
                }
            )

