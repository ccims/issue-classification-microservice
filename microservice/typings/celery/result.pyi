"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager
from kombu.utils.objects import cached_property
from vine import Thenable
from .exceptions import TimeoutError

"""Task results/state and results for groups of tasks."""
E_WOULDBLOCK = """\
Never call result.get() within a task!
See http://docs.celeryq.org/en/latest/userguide/tasks.html\
#task-synchronous-subtasks
"""
def assert_will_not_block():
    ...

@contextmanager
def allow_join_result():
    ...

@contextmanager
def denied_join_result():
    ...

class ResultBase:
    """Base class for results."""
    parent = ...


@Thenable.register
class AsyncResult(ResultBase):
    """Query task state.

    Arguments:
        id (str): See :attr:`id`.
        backend (Backend): See :attr:`backend`.
    """
    app = ...
    TimeoutError = ...
    id = ...
    backend = ...
    def __init__(self, id, backend=..., task_name=..., app=..., parent=...) -> None:
        ...
    
    @property
    def ignored(self):
        """If True, task result retrieval is disabled."""
        ...
    
    @ignored.setter
    def ignored(self, value):
        """Enable/disable task result retrieval."""
        ...
    
    def then(self, callback, on_error=..., weak=...):
        ...
    
    def as_tuple(self):
        ...
    
    def as_list(self):
        """Return as a list of task IDs."""
        ...
    
    def forget(self):
        """Forget the result of this task and its parents."""
        ...
    
    def revoke(self, connection=..., terminate=..., signal=..., wait=..., timeout=...):
        """Send revoke signal to all workers.

        Any worker receiving the task, or having reserved the
        task, *must* ignore it.

        Arguments:
            terminate (bool): Also terminate the process currently working
                on the task (if any).
            signal (str): Name of signal to send to process if terminate.
                Default is TERM.
            wait (bool): Wait for replies from workers.
                The ``timeout`` argument specifies the seconds to wait.
                Disabled by default.
            timeout (float): Time in seconds to wait for replies when
                ``wait`` is enabled.
        """
        ...
    
    def get(self, timeout=..., propagate=..., interval=..., no_ack=..., follow_parents=..., callback=..., on_message=..., on_interval=..., disable_sync_subtasks=..., EXCEPTION_STATES=..., PROPAGATE_STATES=...):
        """Wait until task is ready, and return its result.

        Warning:
           Waiting for tasks within a task may lead to deadlocks.
           Please read :ref:`task-synchronous-subtasks`.

        Warning:
           Backends use resources to store and transmit results. To ensure
           that resources are released, you must eventually call
           :meth:`~@AsyncResult.get` or :meth:`~@AsyncResult.forget` on
           EVERY :class:`~@AsyncResult` instance returned after calling
           a task.

        Arguments:
            timeout (float): How long to wait, in seconds, before the
                operation times out.
            propagate (bool): Re-raise exception if the task failed.
            interval (float): Time to wait (in seconds) before retrying to
                retrieve the result.  Note that this does not have any effect
                when using the RPC/redis result store backends, as they don't
                use polling.
            no_ack (bool): Enable amqp no ack (automatically acknowledge
                message).  If this is :const:`False` then the message will
                **not be acked**.
            follow_parents (bool): Re-raise any exception raised by
                parent tasks.
            disable_sync_subtasks (bool): Disable tasks to wait for sub tasks
                this is the default configuration. CAUTION do not enable this
                unless you must.

        Raises:
            celery.exceptions.TimeoutError: if `timeout` isn't
                :const:`None` and the result does not arrive within
                `timeout` seconds.
            Exception: If the remote call raised an exception then that
                exception will be re-raised in the caller process.
        """
        ...
    
    wait = ...
    def collect(self, intermediate=..., **kwargs):
        """Collect results as they return.

        Iterator, like :meth:`get` will wait for the task to complete,
        but will also follow :class:`AsyncResult` and :class:`ResultSet`
        returned by the task, yielding ``(result, value)`` tuples for each
        result in the tree.

        An example would be having the following tasks:

        .. code-block:: python

            from celery import group
            from proj.celery import app

            @app.task(trail=True)
            def A(how_many):
                return group(B.s(i) for i in range(how_many))()

            @app.task(trail=True)
            def B(i):
                return pow2.delay(i)

            @app.task(trail=True)
            def pow2(i):
                return i ** 2

        .. code-block:: pycon

            >>> from celery.result import ResultBase
            >>> from proj.tasks import A

            >>> result = A.delay(10)
            >>> [v for v in result.collect()
            ...  if not isinstance(v, (ResultBase, tuple))]
            [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        Note:
            The ``Task.trail`` option must be enabled
            so that the list of children is stored in ``result.children``.
            This is the default but enabled explicitly for illustration.

        Yields:
            Tuple[AsyncResult, Any]: tuples containing the result instance
            of the child task, and the return value of that task.
        """
        ...
    
    def get_leaf(self):
        ...
    
    def iterdeps(self, intermediate=...):
        ...
    
    def ready(self):
        """Return :const:`True` if the task has executed.

        If the task is still running, pending, or is waiting
        for retry then :const:`False` is returned.
        """
        ...
    
    def successful(self):
        """Return :const:`True` if the task executed successfully."""
        ...
    
    def failed(self):
        """Return :const:`True` if the task failed."""
        ...
    
    def throw(self, *args, **kwargs):
        ...
    
    def maybe_throw(self, propagate=..., callback=...):
        ...
    
    maybe_reraise = ...
    def build_graph(self, intermediate=..., formatter=...):
        ...
    
    def __str__(self) -> str:
        """`str(self) -> self.id`."""
        ...
    
    def __hash__(self) -> int:
        """`hash(self) -> hash(self.id)`."""
        ...
    
    def __repr__(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __copy__(self):
        ...
    
    def __reduce__(self):
        ...
    
    def __reduce_args__(self):
        ...
    
    def __del__(self):
        """Cancel pending operations when the instance is destroyed."""
        ...
    
    @cached_property
    def graph(self):
        ...
    
    @property
    def supports_native_join(self):
        ...
    
    @property
    def children(self):
        ...
    
    @property
    def result(self):
        """Task return value.

        Note:
            When the task has been executed, this contains the return value.
            If the task raised an exception, this will be the exception
            instance.
        """
        ...
    
    info = ...
    @property
    def traceback(self):
        """Get the traceback of a failed task."""
        ...
    
    @property
    def state(self):
        """The tasks current state.

        Possible values includes:

            *PENDING*

                The task is waiting for execution.

            *STARTED*

                The task has been started.

            *RETRY*

                The task is to be retried, possibly because of failure.

            *FAILURE*

                The task raised an exception, or has exceeded the retry limit.
                The :attr:`result` attribute then contains the
                exception raised by the task.

            *SUCCESS*

                The task executed successfully.  The :attr:`result` attribute
                then contains the tasks return value.
        """
        ...
    
    status = ...
    @property
    def task_id(self):
        """Compat. alias to :attr:`id`."""
        ...
    
    @task_id.setter
    def task_id(self, id):
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def args(self):
        ...
    
    @property
    def kwargs(self):
        ...
    
    @property
    def worker(self):
        ...
    
    @property
    def date_done(self):
        """UTC date and time."""
        ...
    
    @property
    def retries(self):
        ...
    
    @property
    def queue(self):
        ...
    


@Thenable.register
class ResultSet(ResultBase):
    """A collection of results.

    Arguments:
        results (Sequence[AsyncResult]): List of result instances.
    """
    _app = ...
    results = ...
    def __init__(self, results, app=..., ready_barrier=..., **kwargs) -> None:
        ...
    
    def add(self, result):
        """Add :class:`AsyncResult` as a new member of the set.

        Does nothing if the result is already a member.
        """
        ...
    
    def remove(self, result):
        """Remove result from the set; it must be a member.

        Raises:
            KeyError: if the result isn't a member.
        """
        ...
    
    def discard(self, result):
        """Remove result from the set if it is a member.

        Does nothing if it's not a member.
        """
        ...
    
    def update(self, results):
        """Extend from iterable of results."""
        ...
    
    def clear(self):
        """Remove all results from this set."""
        ...
    
    def successful(self):
        """Return true if all tasks successful.

        Returns:
            bool: true if all of the tasks finished
                successfully (i.e. didn't raise an exception).
        """
        ...
    
    def failed(self):
        """Return true if any of the tasks failed.

        Returns:
            bool: true if one of the tasks failed.
                (i.e., raised an exception)
        """
        ...
    
    def maybe_throw(self, callback=..., propagate=...):
        ...
    
    maybe_reraise = ...
    def waiting(self):
        """Return true if any of the tasks are incomplete.

        Returns:
            bool: true if one of the tasks are still
                waiting for execution.
        """
        ...
    
    def ready(self):
        """Did all of the tasks complete? (either by success of failure).

        Returns:
            bool: true if all of the tasks have been executed.
        """
        ...
    
    def completed_count(self):
        """Task completion count.

        Returns:
            int: the number of tasks completed.
        """
        ...
    
    def forget(self):
        """Forget about (and possible remove the result of) all the tasks."""
        ...
    
    def revoke(self, connection=..., terminate=..., signal=..., wait=..., timeout=...):
        """Send revoke signal to all workers for all tasks in the set.

        Arguments:
            terminate (bool): Also terminate the process currently working
                on the task (if any).
            signal (str): Name of signal to send to process if terminate.
                Default is TERM.
            wait (bool): Wait for replies from worker.
                The ``timeout`` argument specifies the number of seconds
                to wait.  Disabled by default.
            timeout (float): Time in seconds to wait for replies when
                the ``wait`` argument is enabled.
        """
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, index):
        """`res[i] -> res.results[i]`."""
        ...
    
    def get(self, timeout=..., propagate=..., interval=..., callback=..., no_ack=..., on_message=..., disable_sync_subtasks=..., on_interval=...):
        """See :meth:`join`.

        This is here for API compatibility with :class:`AsyncResult`,
        in addition it uses :meth:`join_native` if available for the
        current result backend.
        """
        ...
    
    def join(self, timeout=..., propagate=..., interval=..., callback=..., no_ack=..., on_message=..., disable_sync_subtasks=..., on_interval=...):
        """Gather the results of all tasks as a list in order.

        Note:
            This can be an expensive operation for result store
            backends that must resort to polling (e.g., database).

            You should consider using :meth:`join_native` if your backend
            supports it.

        Warning:
            Waiting for tasks within a task may lead to deadlocks.
            Please see :ref:`task-synchronous-subtasks`.

        Arguments:
            timeout (float): The number of seconds to wait for results
                before the operation times out.
            propagate (bool): If any of the tasks raises an exception,
                the exception will be re-raised when this flag is set.
            interval (float): Time to wait (in seconds) before retrying to
                retrieve a result from the set.  Note that this does not have
                any effect when using the amqp result store backend,
                as it does not use polling.
            callback (Callable): Optional callback to be called for every
                result received.  Must have signature ``(task_id, value)``
                No results will be returned by this function if a callback
                is specified.  The order of results is also arbitrary when a
                callback is used.  To get access to the result object for
                a particular id you'll have to generate an index first:
                ``index = {r.id: r for r in gres.results.values()}``
                Or you can create new result objects on the fly:
                ``result = app.AsyncResult(task_id)`` (both will
                take advantage of the backend cache anyway).
            no_ack (bool): Automatic message acknowledgment (Note that if this
                is set to :const:`False` then the messages
                *will not be acknowledged*).
            disable_sync_subtasks (bool): Disable tasks to wait for sub tasks
                this is the default configuration. CAUTION do not enable this
                unless you must.

        Raises:
            celery.exceptions.TimeoutError: if ``timeout`` isn't
                :const:`None` and the operation takes longer than ``timeout``
                seconds.
        """
        ...
    
    def then(self, callback, on_error=..., weak=...):
        ...
    
    def iter_native(self, timeout=..., interval=..., no_ack=..., on_message=..., on_interval=...):
        """Backend optimized version of :meth:`iterate`.

        .. versionadded:: 2.2

        Note that this does not support collecting the results
        for different task types using different backends.

        This is currently only supported by the amqp, Redis and cache
        result backends.
        """
        ...
    
    def join_native(self, timeout=..., propagate=..., interval=..., callback=..., no_ack=..., on_message=..., on_interval=..., disable_sync_subtasks=...):
        """Backend optimized version of :meth:`join`.

        .. versionadded:: 2.2

        Note that this does not support collecting the results
        for different task types using different backends.

        This is currently only supported by the amqp, Redis and cache
        result backends.
        """
        ...
    
    def __len__(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __repr__(self):
        ...
    
    @property
    def supports_native_join(self):
        ...
    
    @property
    def app(self):
        ...
    
    @app.setter
    def app(self, app):
        ...
    
    @property
    def backend(self):
        ...
    


@Thenable.register
class GroupResult(ResultSet):
    """Like :class:`ResultSet`, but with an associated id.

    This type is returned by :class:`~celery.group`.

    It enables inspection of the tasks state and return values as
    a single entity.

    Arguments:
        id (str): The id of the group.
        results (Sequence[AsyncResult]): List of result instances.
        parent (ResultBase): Parent result of this group.
    """
    id = ...
    results = ...
    def __init__(self, id=..., results=..., parent=..., **kwargs) -> None:
        ...
    
    def save(self, backend=...):
        """Save group-result for later retrieval using :meth:`restore`.

        Example:
            >>> def save_and_restore(result):
            ...     result.save()
            ...     result = GroupResult.restore(result.id)
        """
        ...
    
    def delete(self, backend=...):
        """Remove this result if it was previously saved."""
        ...
    
    def __reduce__(self):
        ...
    
    def __reduce_args__(self):
        ...
    
    def __bool__(self):
        ...
    
    __nonzero__ = ...
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self) -> str:
        """`str(self) -> self.id`."""
        ...
    
    def __hash__(self) -> int:
        """`hash(self) -> hash(self.id)`."""
        ...
    
    def as_tuple(self):
        ...
    
    @property
    def children(self):
        ...
    
    @classmethod
    def restore(cls, id, backend=..., app=...):
        """Restore previously saved group result."""
        ...
    


@Thenable.register
class EagerResult(AsyncResult):
    """Result that we know has already been executed."""
    def __init__(self, id, ret_value, state, traceback=...) -> None:
        ...
    
    def then(self, callback, on_error=..., weak=...):
        ...
    
    def __reduce__(self):
        ...
    
    def __reduce_args__(self):
        ...
    
    def __copy__(self):
        ...
    
    def ready(self):
        ...
    
    def get(self, timeout=..., propagate=..., disable_sync_subtasks=..., **kwargs):
        ...
    
    wait = ...
    def forget(self):
        ...
    
    def revoke(self, *args, **kwargs):
        ...
    
    def __repr__(self):
        ...
    
    @property
    def result(self):
        """The tasks return value."""
        ...
    
    @property
    def state(self):
        """The tasks state."""
        ...
    
    status = ...
    @property
    def traceback(self):
        """The traceback if the task failed."""
        ...
    
    @property
    def supports_native_join(self):
        ...
    


def result_from_tuple(r, app=...):
    """Deserialize result from tuple."""
    ...

