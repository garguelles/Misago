from ...users.bans import get_user_ban
from ...users.models import Rank
from ..user import (
    PASSWORD,
    get_fake_admin_activated_user,
    get_fake_banned_user,
    get_fake_inactive_user,
    get_fake_user,
)


def test_fake_user_can_be_created(db, fake):
    assert get_fake_user(fake)


def test_fake_user_is_created_with_predictable_password(db, fake):
    user = get_fake_user(fake)
    assert user.check_password(PASSWORD)


def test_fake_user_is_created_with_test_avatars(db, fake):
    user = get_fake_user(fake)
    assert user.avatars


def test_fake_user_is_created_with_explicit_rank(db, fake):
    rank = Rank.objects.create(name="Test Rank")
    user = get_fake_user(fake, rank)
    assert user.rank is rank


def test_banned_fake_user_can_be_created(db, cache_versions, fake):
    user = get_fake_banned_user(fake)
    assert get_user_ban(user, cache_versions)


def test_inactivate_fake_user_can_be_created(db, fake):
    user = get_fake_inactive_user(fake)
    assert user.requires_activation


def test_admin_activated_fake_user_can_be_created(db, fake):
    user = get_fake_admin_activated_user(fake)
    assert user.requires_activation
