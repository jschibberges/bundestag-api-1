# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from dataclasses import dataclass
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
import urllib3
from bundestag import schemas  # noqa: F401
from bundestag import api_client, exceptions
from urllib3._collections import HTTPHeaderDict

# query params
ContentIdSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    "RequestRequiredQueryParams",
    {
        "contentId": typing.Union[
            ContentIdSchema,
            decimal.Decimal,
            int,
        ],
    },
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    "RequestOptionalQueryParams", {}, total=False
)

class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass

request_query_content_id = api_client.QueryParameter(
    name="contentId",
    style=api_client.ParameterStyle.FORM,
    schema=ContentIdSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationXml = schemas.StrSchema

@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationXml,
    ]
    headers: schemas.Unset = schemas.unset

_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        "application/xml": api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml
        ),
    },
)
_all_accept_content_types = ("application/xml",)

class BaseApi(api_client.Api):
    def _iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization]:
        """
        Abruf eines Videos
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (request_query_content_id,):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(
                parameter_data, prefix_separator_iterator
            )
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add("Accept", accept_content_type)

        host = self._get_host_oapg(
            "iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get",
            _servers,
            host_index,
        )

        response = self.api_client.call_api(
            resource_path=used_path,
            method="get".upper(),
            headers=_headers,
            host=host,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(
                response=response
            )
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(
                    response, self.api_client.configuration
                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response
                )

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response

class IptvPlayerMacrosXs144277506BttvMobileFeedVodXmlGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization]:
        return self._iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            host_index=host_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )

class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization]:
        return self._iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            host_index=host_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
