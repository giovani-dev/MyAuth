
from datetime import datetime
from typing import Optional
from unittest.mock import patch
from uuid import UUID, uuid4
from MyAuth.Application.Data.Dto.user import IsertUserDto, UpdateUserDto, UserDto
from MyAuth.Infrastructure.Database.Repository.user_repository import UserRepository
from MyAuth.Infrastructure.Database.Model.user import User
import pytest


class BaseUserRepositoryTest(object):
    _repository: UserRepository
    _data: IsertUserDto
    _user: Optional[UserDto] = None
    _another_user: Optional[UserDto] = None
    _delete_in_teardown = True

    def setup_method(self):
        self._data = IsertUserDto(
            name='Roberto Augusto',
            email='augusto@email.com',
            cellphone='47993920628',
            user_name='augusto@email.com',
            password='123',
            password_verification='123'
        )
        self._repository = UserRepository()

    def teardown_method(self):
        if self._user and self._delete_in_teardown:
            query = User.get(User.external_id == self._user.id)
            query.delete_instance()
        if self._another_user and self._delete_in_teardown:
            self._another_user.delete_instance()


class TestUserRepositoryCreateUser(BaseUserRepositoryTest):

    @pytest.mark.asyncio
    @pytest.mark.freeze_time
    @patch('MyAuth.Infrastructure.Database.Repository.user_repository.uuid4')
    async def test_create_user__compare_with_user_input__expected_data_saved_in_table(
        self,
        mock_uuid4,
        freezer,
    ):
        mock_uuid4.return_value = UUID('1c275661-fa2b-40b7-b706-9d24b24d2ac4')
        self._user = await self._repository.create(self._data)

        assert self._user
        assert self._user.name == self._data.name
        assert self._user.email == self._data.email
        assert self._user.cellphone == self._data.cellphone
        assert self._user.user_name == self._data.user_name
        assert self._user.id == UUID('1c275661-fa2b-40b7-b706-9d24b24d2ac4')
        assert self._user.creation_date == datetime.now().replace(microsecond=0)
        assert not self._user.updated_date

    @pytest.mark.asyncio
    async def test_create_user__verify_types__expected_repository_return_with_correct_types(
        self
    ):
        self._user = await self._repository.create(self._data)

        assert isinstance(self._user.id, UUID)
        assert isinstance(self._user.name, str)
        assert isinstance(self._user.email, str)
        assert isinstance(self._user.user_name, str)
        assert isinstance(self._user.cellphone, str)
        assert isinstance(self._user.creation_date, datetime)
        assert isinstance(self._user.updated_date, type(None))

    @pytest.mark.asyncio
    async def test_create_user__verify_database_data_persisted__expected_data_persisted(self):
        self._user = await self._repository.create(self._data)
        compare_query = User.get_or_none(User.external_id == self._user.id)

        assert self._user
        assert compare_query
        assert self._user.id == UUID(compare_query.external_id)
        assert self._user.name == compare_query.name
        assert self._user.email == compare_query.email
        assert self._user.user_name == compare_query.user_name
        assert self._user.cellphone == compare_query.cellphone
        assert compare_query.is_adm == False
        assert self._user.creation_date == compare_query.creation_date
        assert self._user.updated_date == compare_query.updated_date

    @pytest.mark.asyncio
    async def teste_create_adm_user__verify_database_data_persisted__expected_data_persisted(
        self
    ):
        self._user = await self._repository.create(self._data, is_adm=True)
        compare_query = User.get_or_none(User.external_id == self._user.id)

        assert self._user
        assert compare_query
        assert self._user.id == UUID(compare_query.external_id)
        assert self._user.name == compare_query.name
        assert self._user.email == compare_query.email
        assert self._user.user_name == compare_query.user_name
        assert self._user.cellphone == compare_query.cellphone
        assert compare_query.is_adm == True
        assert self._user.creation_date == compare_query.creation_date
        assert self._user.updated_date == compare_query.updated_date

    @pytest.mark.asyncio
    async def test_create_adm_user__create_with_same_email__expected_not_created(
        self
    ):
        self._user = await self._repository.create(self._data, is_adm=True)
        self._another_user = await self._repository.create(
            data=IsertUserDto(
                name='Xi Jinping',
                email=self._user.email,
                cellphone='99999999999',
                user_name='JinJin',
                password='123',
                password_verification='123'
            ),
            is_adm=True
        )
        compare_query = User.select().where(User.email == self._user.email)
        compare_query = list(compare_query)

        assert not self._another_user
        assert len(compare_query) == 1


class TestUserRepositoryUpdateUser(BaseUserRepositoryTest):
    
    @pytest.mark.freeze_time
    @pytest.mark.asyncio
    async def test_update_user__update_one_user_name_field__expected_data_updated(
        self
    ):
        self._user = await self._repository.create(self._data)
        user_updated = await self._repository.update(
            id=self._user.id,
            data=UpdateUserDto(
                name='Nome atualizado'
            )
        )
        compare_query = User.get(User.external_id == user_updated.id)

        assert user_updated.name == 'Nome atualizado'
        assert user_updated.name != self._user.name
        assert user_updated.name == compare_query.name

        assert user_updated.updated_date == datetime.now().replace(microsecond=0)
        assert user_updated.updated_date != self._user.updated_date
        assert user_updated.updated_date == compare_query.updated_date

        assert user_updated.id == UUID(compare_query.external_id)
        assert user_updated.id == self._user.id
        assert user_updated.id == user_updated.id

    @pytest.mark.asyncio
    async def test_update_user__update_all_fields__expected_data_updated(
        self
    ):
        self._user = await self._repository.create(self._data)
        user_updated = await self._repository.update(
            id=self._user.id,
            data=UpdateUserDto(
                name='Nome atualizado',
                email='novo@email.com',
                cellphone='9999999999',
                user_name='novo nome de usuario'
            )
        )
        compare_query = User.get(User.external_id == user_updated.id)

        assert user_updated.name == 'Nome atualizado'
        assert user_updated.name != self._user.name
        assert user_updated.name == compare_query.name

        assert user_updated.email == 'novo@email.com'
        assert user_updated.email != self._user.email
        assert user_updated.email == compare_query.email

        assert user_updated.cellphone == '9999999999'
        assert user_updated.cellphone != self._user.cellphone
        assert user_updated.cellphone == compare_query.cellphone

        assert user_updated.user_name == 'novo nome de usuario'
        assert user_updated.user_name != self._user.user_name
        assert user_updated.user_name == compare_query.user_name

        assert user_updated.updated_date == datetime.now().replace(microsecond=0)
        assert user_updated.updated_date != self._user.updated_date
        assert user_updated.updated_date == compare_query.updated_date

        assert user_updated.id == UUID(compare_query.external_id)
        assert user_updated.id == self._user.id
        assert user_updated.id == user_updated.id

    @pytest.mark.asyncio
    async def test_update_adm_user__update_non_existed_user__expected_return_none(
        self
    ):
        user_updated = await self._repository.update(
            id=UUID('1c275661-fa2b-40b7-b706-9d24b24d2ac4'),
            data=UpdateUserDto(
                name='Nome atualizado',
                email='novo@email.com',
                cellphone='9999999999',
                user_name='novo nome de usuario'
            )
        )

        assert not user_updated


class TestUserRepositoryRetrieveUser(BaseUserRepositoryTest):

    @pytest.mark.asyncio
    async def test_get_one_by_id__retrieve_non_existed_user__expected_none_return(
        self
    ):
        self._user = await self._repository.get_one_by_id(
            id=UUID('1c275661-fa2b-40b7-b706-9d24b24d2ac4')
        )

        assert not self._user

    @pytest.mark.asyncio
    @pytest.mark.freeze_time
    async def test_get_one_by_id__retrieve_user__expected_user_dto_return(
        self
    ):
        self._user = await self._repository.create(self._data)
        retrieved_user = await self._repository.get_one_by_id(
            id=self._user.id
        )

        assert retrieved_user.name == self._data.name
        assert retrieved_user.email == self._data.email
        assert retrieved_user.cellphone == self._data.cellphone
        assert retrieved_user.user_name == self._data.user_name
        assert retrieved_user.creation_date == datetime.now().replace(microsecond=0)
        assert retrieved_user.updated_date == None

    # --------------------------------

    @pytest.mark.asyncio
    async def test_get_one_by_email__retrieve_non_existed_user__expected_none_return(
        self
    ):
        self._user = await self._repository.get_one_by_email(
            email='naoexiste@email.com'
        )

        assert not self._user

    @pytest.mark.asyncio
    @pytest.mark.freeze_time
    async def test_get_one_by_email__retrieve_user__expected_user_dto_return(
        self
    ):
        self._user = await self._repository.create(self._data)
        retrieved_user = await self._repository.get_one_by_email(
            email=self._user.email
        )

        assert retrieved_user.name == self._data.name
        assert retrieved_user.email == self._data.email
        assert retrieved_user.cellphone == self._data.cellphone
        assert retrieved_user.user_name == self._data.user_name
        assert retrieved_user.creation_date == datetime.now().replace(microsecond=0)
        assert retrieved_user.updated_date == None

    # --------------------------------

    @pytest.mark.asyncio
    async def test_get_one_by_user_name__retrieve_non_existed_user__expected_none_return(
        self
    ):
        self._user = await self._repository.get_one_by_user_name(
            user_name='naoexiste'
        )

        assert not self._user

    @pytest.mark.asyncio
    @pytest.mark.freeze_time
    async def test_get_one_by_user_name__retrieve_user__expected_user_dto_return(
        self
    ):
        self._user = await self._repository.create(self._data)
        retrieved_user = await self._repository.get_one_by_user_name(
            user_name=self._user.user_name
        )

        assert retrieved_user.name == self._data.name
        assert retrieved_user.email == self._data.email
        assert retrieved_user.cellphone == self._data.cellphone
        assert retrieved_user.user_name == self._data.user_name
        assert retrieved_user.creation_date == datetime.now().replace(microsecond=0)
        assert retrieved_user.updated_date == None


class TestUserRepositoryDeleteUser(BaseUserRepositoryTest):

    @pytest.mark.asyncio
    async def test_delete__delete_non_existed_user__expected_false_return(
        self
    ):
        deleted_user = await self._repository.delete(
            id=UUID('1c275661-fa2b-40b7-b706-9d24b24d2ac4')
        )

        assert not deleted_user
        assert isinstance(deleted_user, bool)

    @pytest.mark.asyncio
    async def test_delete__delete_user__expected_true_return(
        self
    ):
        self._delete_in_teardown = False
        self._user = await self._repository.create(self._data)
        delete_user = await self._repository.delete(
            id=self._user.id
        )

        assert delete_user
        assert isinstance(delete_user, bool)
