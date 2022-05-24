''' Service Sync '''
import logging

from module.gsuite import GSuite


class SyncGSuite(GSuite):
    ''' Sync GSuite

    :param str credentialfile: credentialfile path
    :param str with_subject: admin user

    '''

    def __init__(self, credentialfile: str, with_subject: str) -> None:
        super().__init__(
            credentialfile=credentialfile, with_subject=with_subject)

    def add_users_into_group(self, group: str, users: list[str]) -> None:
        ''' Add some users into one group

        :param str group: group_key or mail
        :param list users: users's mail

        '''
        group_info = self.groups_get(group_key=group)

        for user in users:
            if self.members_has_member(group_key=group_info['id'], email=user)['isMember']:
                logging.info('[%s] isMember: True', user)
            else:
                logging.info('Add [%s] into [%s]', user, group_info['id'])
                self.members_insert(group_key=group_info['id'], email=user)

    def del_users_from_group(self, group: str, users: list[str]) -> None:
        ''' del some users from one group

        :param str group: group_key or mail
        :param list users: users's mail

        '''
        group_info = self.groups_get(group_key=group)

        for user in users:
            if self.members_has_member(group_key=group_info['id'], email=user)['isMember']:
                logging.info('del [%s] from [%s]', user, group_info['id'])
                self.members_delete(group_key=group_info['id'], email=user)
            else:
                logging.info('[%s] isMember: False', user)
