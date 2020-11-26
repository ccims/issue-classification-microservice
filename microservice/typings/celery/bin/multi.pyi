"""
This type stub file was generated by pyright.
"""

import click
from kombu.utils.objects import cached_property
from celery.apps.multi import MultiParser
from celery.bin.base import CeleryCommand

"""Start multiple worker instances from the command-line.

.. program:: celery multi

Examples
========

.. code-block:: console

    $ # Single worker with explicit name and events enabled.
    $ celery multi start Leslie -E

    $ # Pidfiles and logfiles are stored in the current directory
    $ # by default.  Use --pidfile and --logfile argument to change
    $ # this.  The abbreviation %n will be expanded to the current
    $ # node name.
    $ celery multi start Leslie -E --pidfile=/var/run/celery/%n.pid
                                   --logfile=/var/log/celery/%n%I.log


    $ # You need to add the same arguments when you restart,
    $ # as these aren't persisted anywhere.
    $ celery multi restart Leslie -E --pidfile=/var/run/celery/%n.pid
                                     --logfile=/var/log/celery/%n%I.log

    $ # To stop the node, you need to specify the same pidfile.
    $ celery multi stop Leslie --pidfile=/var/run/celery/%n.pid

    $ # 3 workers, with 3 processes each
    $ celery multi start 3 -c 3
    celery worker -n celery1@myhost -c 3
    celery worker -n celery2@myhost -c 3
    celery worker -n celery3@myhost -c 3

    $ # override name prefix when using range
    $ celery multi start 3 --range-prefix=worker -c 3
    celery worker -n worker1@myhost -c 3
    celery worker -n worker2@myhost -c 3
    celery worker -n worker3@myhost -c 3

    $ # start 3 named workers
    $ celery multi start image video data -c 3
    celery worker -n image@myhost -c 3
    celery worker -n video@myhost -c 3
    celery worker -n data@myhost -c 3

    $ # specify custom hostname
    $ celery multi start 2 --hostname=worker.example.com -c 3
    celery worker -n celery1@worker.example.com -c 3
    celery worker -n celery2@worker.example.com -c 3

    $ # specify fully qualified nodenames
    $ celery multi start foo@worker.example.com bar@worker.example.com -c 3

    $ # fully qualified nodenames but using the current hostname
    $ celery multi start foo@%h bar@%h

    $ # Advanced example starting 10 workers in the background:
    $ #   * Three of the workers processes the images and video queue
    $ #   * Two of the workers processes the data queue with loglevel DEBUG
    $ #   * the rest processes the default' queue.
    $ celery multi start 10 -l INFO -Q:1-3 images,video -Q:4,5 data
        -Q default -L:4,5 DEBUG

    $ # You can show the commands necessary to start the workers with
    $ # the 'show' command:
    $ celery multi show 10 -l INFO -Q:1-3 images,video -Q:4,5 data
        -Q default -L:4,5 DEBUG

    $ # Additional options are added to each celery worker' comamnd,
    $ # but you can also modify the options for ranges of, or specific workers

    $ # 3 workers: Two with 3 processes, and one with 10 processes.
    $ celery multi start 3 -c 3 -c:1 10
    celery worker -n celery1@myhost -c 10
    celery worker -n celery2@myhost -c 3
    celery worker -n celery3@myhost -c 3

    $ # can also specify options for named workers
    $ celery multi start image video data -c 3 -c:image 10
    celery worker -n image@myhost -c 10
    celery worker -n video@myhost -c 3
    celery worker -n data@myhost -c 3

    $ # ranges and lists of workers in options is also allowed:
    $ # (-c:1-3 can also be written as -c:1,2,3)
    $ celery multi start 5 -c 3  -c:1-3 10
    celery worker -n celery1@myhost -c 10
    celery worker -n celery2@myhost -c 10
    celery worker -n celery3@myhost -c 10
    celery worker -n celery4@myhost -c 3
    celery worker -n celery5@myhost -c 3

    $ # lists also works with named workers
    $ celery multi start foo bar baz xuzzy -c 3 -c:foo,bar,baz 10
    celery worker -n foo@myhost -c 10
    celery worker -n bar@myhost -c 10
    celery worker -n baz@myhost -c 10
    celery worker -n xuzzy@myhost -c 3
"""
USAGE = """\
usage: {prog_name} start <node1 node2 nodeN|range> [worker options]
       {prog_name} stop <n1 n2 nN|range> [-SIG (default: -TERM)]
       {prog_name} restart <n1 n2 nN|range> [-SIG] [worker options]
       {prog_name} kill <n1 n2 nN|range>

       {prog_name} show <n1 n2 nN|range> [worker options]
       {prog_name} get hostname <n1 n2 nN|range> [-qv] [worker options]
       {prog_name} names <n1 n2 nN|range>
       {prog_name} expand template <n1 n2 nN|range>
       {prog_name} help

additional options (must appear after command name):

    * --nosplash:   Don't display program info.
    * --quiet:      Don't show as much output.
    * --verbose:    Show more output.
    * --no-color:   Don't display colors.
"""
def main():
    ...

def splash(fun):
    ...

def using_cluster(fun):
    ...

def using_cluster_and_sig(fun):
    ...

class TermLogger:
    splash_text = ...
    splash_context = ...
    retcode = ...
    def setup_terminal(self, stdout, stderr, nosplash=..., quiet=..., verbose=..., no_color=..., **kwargs):
        ...
    
    def ok(self, m, newline=..., file=...):
        ...
    
    def say(self, m, newline=..., file=...):
        ...
    
    def carp(self, m, newline=..., file=...):
        ...
    
    def error(self, msg=...):
        ...
    
    def info(self, msg, newline=...):
        ...
    
    def note(self, msg, newline=...):
        ...
    
    @splash
    def usage(self):
        ...
    
    def splash(self):
        ...
    
    @cached_property
    def colored(self):
        ...
    


class MultiTool(TermLogger):
    """The ``celery multi`` program."""
    MultiParser = ...
    OptionParser = ...
    reserved_options = ...
    def __init__(self, env=..., cmd=..., fh=..., stdout=..., stderr=..., **kwargs) -> None:
        ...
    
    def execute_from_commandline(self, argv, cmd=...):
        ...
    
    def validate_arguments(self, argv):
        ...
    
    def call_command(self, command, argv):
        ...
    
    @splash
    @using_cluster
    def start(self, cluster):
        ...
    
    @splash
    @using_cluster_and_sig
    def stop(self, cluster, sig, **kwargs):
        ...
    
    @splash
    @using_cluster_and_sig
    def stopwait(self, cluster, sig, **kwargs):
        ...
    
    stop_verify = ...
    @splash
    @using_cluster_and_sig
    def restart(self, cluster, sig, **kwargs):
        ...
    
    @using_cluster
    def names(self, cluster):
        ...
    
    def get(self, wanted, *argv):
        ...
    
    @using_cluster
    def show(self, cluster):
        ...
    
    @splash
    @using_cluster
    def kill(self, cluster):
        ...
    
    def expand(self, template, *argv):
        ...
    
    def help(self, *argv):
        ...
    
    def cluster_from_argv(self, argv, cmd=...):
        ...
    
    def Cluster(self, nodes, cmd=...):
        ...
    
    def on_stopping_preamble(self, nodes):
        ...
    
    def on_send_signal(self, node, sig):
        ...
    
    def on_still_waiting_for(self, nodes):
        ...
    
    def on_still_waiting_progress(self, nodes):
        ...
    
    def on_still_waiting_end(self):
        ...
    
    def on_node_signal_dead(self, node):
        ...
    
    def on_node_start(self, node):
        ...
    
    def on_node_restart(self, node):
        ...
    
    def on_node_down(self, node):
        ...
    
    def on_node_shutdown_ok(self, node):
        ...
    
    def on_node_status(self, node, retval):
        ...
    
    def on_node_signal(self, node, sig):
        ...
    
    def on_child_spawn(self, node, argstr, env):
        ...
    
    def on_child_signalled(self, node, signum):
        ...
    
    def on_child_failure(self, node, retcode):
        ...
    
    @cached_property
    def OK(self):
        ...
    
    @cached_property
    def FAILED(self):
        ...
    
    @cached_property
    def DOWN(self):
        ...
    


@click.command(cls=CeleryCommand, context_settings={ 'allow_extra_args': True,'ignore_unknown_options': True })
@click.pass_context
def multi(ctx):
    """Start multiple worker instances."""
    ...
