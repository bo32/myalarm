# from tkinter import *

# import gst

# class VideoPlayer(Frame):

#     def __init__(self, container):

#         player = gst.element_factory_make('playbin2', 'player')
#         player.set_property('video-sink', None)
#         player.set_property('uri', 'file:///home/david/Videos/Cartoons/Bye Bye Bunny-69228454.mp4')
#         player.set_state(gst.STATE_PLAYING)

#         bus = player.get_bus()
#         bus.add_signal_watch()
#         bus.enable_sync_message_emission()
#         bus.connect('sync-message::element', self.on_sync_message, self.window_id())

#     def on_sync_message(self, bus, message, window_id):
#         if not message.structure is None:
#             if message.structure.get_name() == 'prepare-xwindow-id':
#                 image_sink = message.src
#                 image_sink.set_property('force-aspect-ratio', True)
#                 image_sink.set_xwindow_id(window_id)