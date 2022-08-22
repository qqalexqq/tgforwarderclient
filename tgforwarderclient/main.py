from click import group, option
from pyrogram import Client
from tgforwarderclient.app import make_app


@group()
def cli_main() -> None:
    pass


@cli_main.command(
    name="run",
    help="Run forwarder",
    context_settings=dict(
        auto_envvar_prefix="bot",
        show_default=True,
    ),
)
@option(
    "--api_id",
    help="Client's api_id",
    required=True,
    type=int,
    allow_from_autoenv=True,
)
@option(
    "--api_hash",
    help="Client's api_hash",
    required=True,
    allow_from_autoenv=True,
)
@option(
    "--session_key",
    "--session",
    help="Session key",
    required=True,
    allow_from_autoenv=True,
)
@option(
    "--channels",
    "--channel",
    help="One or more channels for listening",
    required=True,
    allow_from_autoenv=True,
    multiple=True,
)
@option(
    "--chats",
    "--chat",
    help="One or more chats for message forwarding",
    required=True,
    allow_from_autoenv=True,
    type=int,
    multiple=True,
)
@option(
    "--session_name",
    help="Session name",
    required=False,
    default="forwarder_account",
    show_default=True,
    allow_from_autoenv=True,
)
def run_command(
    session_name: str,
    api_id: int,
    api_hash: str,
    session_key: str,
    channels: list[str],
    chats: list[int],
) -> None:
    app = make_app(
        session_name=session_name,
        api_id=api_id,
        api_hash=api_hash,
        session_key=session_key,
        channels=channels,
        chats=chats,
    )
    app.run()


@cli_main.command(
    name="export",
    help="Export session string",
    context_settings=dict(
        auto_envvar_prefix="bot",
        show_default=True,
    ),
)
@option(
    "--api_id",
    help="Client's api_id",
    required=True,
    type=int,
    allow_from_autoenv=True,
)
@option(
    "--api_hash",
    help="Client's api_hash",
    required=True,
    allow_from_autoenv=True,
)
@option(
    "--session_name",
    help="Session name",
    required=False,
    default="forwarder_account",
    show_default=True,
    allow_from_autoenv=True,
)
def run_exporter(
    api_id: int,
    api_hash: str,
    session_name: str,
) -> None:
    with Client(session_name, api_id, api_hash) as app:
        print("---")
        session_string = app.export_session_string()
        print(f"Session key is: {session_string!r}")
