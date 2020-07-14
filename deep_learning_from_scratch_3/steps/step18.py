import contextlib


class Config:
    # class 変数
    enable_backdrop: bool = False


@contextlib.contextmanager
def using_config(name: str, value: str) -> None:
    old_value: bool = getattr(Config, name)
    setattr(Config, name, value)
    try:
        yield
    finally:
        setattr(Config, name, old_value)
