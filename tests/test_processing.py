import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize(
    "operation, state, result",
    [
        ("operations", None, "executed_operations"),
        ("operations", "EXECUTED", "executed_operations"),
        ("operations", "CANCELED", "canceled_operations"),
    ],
)
def test_filter_by_state_normal(operation: list[dict], state: str, result: list[dict], request) -> None:
    # Если state == None, подставляем значение по умолчанию "EXECUTED"
    state = state if state is not None else "EXECUTED"
    assert filter_by_state(request.getfixturevalue(operation), state) == request.getfixturevalue(result)
