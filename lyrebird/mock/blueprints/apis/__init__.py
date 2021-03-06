from flask import Blueprint, request
from flask_restful import Resource, Api
from .common import Status, WorkMode, Manifest
from .flow import Flow, FlowList
from .mock import MockData, MockGroup, ActivatedMockGroup, MockGroupByName
from .config import Conf, ResetConf
from .plugin import Plugin
from .menu import Menu
from .notice import Notice
from .checker import Checker
from .event import Event, Channel
from .conflict_check import ConflictCheck, ActivatedDataConflictCheck
from .mock_editor import Cut, Copy, Paste
from .search import SearchMockDataByName
from lyrebird.log import get_logger
from lyrebird import application
from flask import got_request_exception
import traceback


logger = get_logger()


api = Blueprint('api', __name__, url_prefix='/api')
api_source = Api(api, errors=Exception)


@api.after_request
def after_request(response):
    """
    输出每条请求概要信息
    """
    lyrebird_info = response.headers.get('lyrebird', default='')
    logger.debug(f'[On API]{response.status_code} {lyrebird_info} {request.method} {request.url[:100]}')
    return response


@api.errorhandler(Exception)
def on_500(error):
    return application.make_fail_response(f'{error.__class__.__name__} {error}')


api_source.add_resource(Status, '/status')
api_source.add_resource(Manifest, '/manifest')
api_source.add_resource(Flow, '/flow/<string:id>')
api_source.add_resource(FlowList, '/flow')
api_source.add_resource(Cut, '/cut/<string:_id>')
api_source.add_resource(Copy, '/copy/<string:_id>')
api_source.add_resource(Paste, '/paste/<string:_id>')
api_source.add_resource(MockGroup, '/group', '/group/<string:group_id>')
api_source.add_resource(MockData, '/data', '/data/<string:_id>')
api_source.add_resource(SearchMockDataByName, '/search/group/name/', '/search/group/name/<string:search_str>')
api_source.add_resource(ConflictCheck, '/conflict/id/<string:group_id>')
api_source.add_resource(ActivatedDataConflictCheck, '/conflict/activated')
api_source.add_resource(ActivatedMockGroup, '/mock/activated', '/mock/<string:group_id>/<string:action>')
api_source.add_resource(MockGroupByName, '/mock_by_name')
api_source.add_resource(Conf, '/conf/<string:plugin_name>')
api_source.add_resource(ResetConf, '/conf/<string:plugin_name>/reset')
api_source.add_resource(WorkMode, '/mode', '/mode/<string:mode>')
api_source.add_resource(Plugin, '/plugin', '/plugin/<string:plugin_name>')
api_source.add_resource(Menu, '/menu')
api_source.add_resource(Notice, '/notice')
api_source.add_resource(Checker, '/checker', '/checker/<string:checker_id>')
api_source.add_resource(
    Event,
    '/event',
    '/event/page/<int:page>',
    '/event/id/<string:event_id>',
    '/event/<string:channel>',
    '/event/<string:channel>/page/<int:page>',
    '/event/<string:channel>/id/<string:event_id>'
)
api_source.add_resource(Channel, '/channel')
