#!/usr/bin/env python3
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec={
            'message': {'type':'str', 'required': True}
        }
    )

    message = module.params['message']
    reversed_message = message[::-1]

    if message == 'fail me':
        module.fail_json(
            msg='You requested this to fail',
            changed=True,
            original_message=message,
            reversed_message=reversed_message
        )

    changed = message != reversed_message

    module.exit_json(
        changed=changed,
        original_message=message,
        reversed_message=reversed_message
    )

if __name__ == '__main__':
    main()