"""
This type stub file was generated by pyright.
"""

import click
from celery.bin.base import CeleryDaemonCommand, CeleryOption, LOG_LEVEL

"""The :program:`celery beat` command."""
@click.command(cls=CeleryDaemonCommand, context_settings={ 'allow_extra_args': True })
@click.option('--detach', cls=CeleryOption, is_flag=True, default=False, help_group="Beat Options", help="Detach and run in the background as a daemon.")
@click.option('-s', '--schedule', cls=CeleryOption, callback=lambda ctx, _, value: value or ctx.obj.app.conf.beat_schedule_filename, help_group="Beat Options", help="Path to the schedule database." "  Defaults to `celerybeat-schedule`." "The extension '.db' may be appended to the filename.")
@click.option('-S', '--scheduler', cls=CeleryOption, callback=lambda ctx, _, value: value or ctx.obj.app.conf.beat_scheduler, help_group="Beat Options", help="Scheduler class to use.")
@click.option('--max-interval', cls=CeleryOption, type=int, help_group="Beat Options", help="Max seconds to sleep between schedule iterations.")
@click.option('-l', '--loglevel', default='WARNING', cls=CeleryOption, type=LOG_LEVEL, help_group="Beat Options", help="Logging level.")
@click.pass_context
def beat(ctx, detach=..., logfile=..., pidfile=..., uid=..., gid=..., umask=..., workdir=..., **kwargs):
    """Start the beat periodic task scheduler."""
    ...

