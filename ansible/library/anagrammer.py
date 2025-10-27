#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

module = AnsibleModule(
    argument_spec=dict(
        message=dict(type="str", required=False, default="This is default string!")
    )
)

original_text = module.params["message"]
reversed_text = "".join(reversed(original_text))

if original_text == reversed_text:
    module.exit_json(
        changed=False, original_text=original_text, reversed_text=reversed_text
    )

elif original_text == "fail me":
    module.exit_json(
        changed=True,
        msg="You requested this to fail",
        original_text=original_text,
        reversed_text=reversed_text,
    )

else:
    module.exit_json(
        changed=True, original_text=original_text, reversed_text=reversed_text
    )
