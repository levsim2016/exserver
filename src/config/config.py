from pydantic import BaseModel, AnyHttpUrl, IPvAnyAddress, Union, PositiveInt, StrictBool, ConfigDict


def lower_env_var_name(var_name: str):
    return var_name.lower()


class ConfigModel(BaseModel):
    model_config = ConfigDict(alias_generator=lower_env_var_name)

    host_dev: Union[AnyHttpUrl, IPvAnyAddress]
    host_prod: Union[AnyHttpUrl, IPvAnyAddress]
    port: PositiveInt
    reload: StrictBool
    production: StrictBool
