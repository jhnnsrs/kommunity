from arkitekt import easy, register

from unlok.api.schema import notify_user
from rekuest.actors.vars import get_current_assignation_helper


@register
def notify_me(title: str, message: str) -> str:
    """Notify me of something

    Notify me of something

    Args:
        image (RepresentationFragment): The image
        fps (int, optional): The frames per stack. Defaults to 2.

    Returns:
        VideoFragment: The video
    """
    user = get_current_assignation_helper().user
    print(user)
    print(notify_user(2, message=message, title=title))
    return "Okey"


