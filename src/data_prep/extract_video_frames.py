from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from absl import logging
import cv2
import itertools
import math
import os


FLAGS = flags.FLAGS
flags.DEFINE_string('file', None, 'Video file to extract frame data from.')
flags.DEFINE_string('outdir', None, 'Output directory to write frame data to.')

flags.DEFINE_float(
    'start_time', None,
    'Time to start capturing data from. If not specified, will default to 0.')
flags.DEFINE_float(
    'end_time', None,
    'Time to stop capturing data from. If not specified, will default to the '
    'end of the video file.')
flags.DEFINE_integer('frame_step', 1, 'Step while iterating over frames.')

# Required flags
flags.mark_flag_as_required('file')
flags.mark_flag_as_required('outdir')


def iterate_over_frames(video):
  frame_number = 0
  success = True

  while success:
    success, frame = video.read()
    if not success:
      raise RuntimeError('Failed to read frame %d' % frame_number)

    yield frame_number, frame
    frame_number += 1


def main(argv):
  del argv

  video = cv2.VideoCapture(FLAGS.file)
  if not video.isOpened():
    raise ValueError('Failed to open file: ' + FLAGS.file)
  logging.info('File loaded successfully.')

  total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  logging.info('Video total frames: %d', total_frames)

  fps = int(video.get(cv2.CAP_PROP_FPS))
  logging.info('Video FPS: %d', fps)

  start_frame = 0
  if FLAGS.start_time is not None:
    start_frame = math.ceil(FLAGS.start_time * fps)

  end_frame = total_frames - 1
  if FLAGS.end_time is not None:
    end_frame = math.floor(FLAGS.end_time * fps)

  logging.info('Starting capture on frame: %d', start_frame)
  logging.info('Ending capture on frame: %d', end_frame)

  frames = itertools.islice(
      iterate_over_frames(video), start_frame, end_frame, FLAGS.frame_step)
  for i, frame in frames:
    cv2.imwrite(
        os.path.join(FLAGS.outdir, 'frame:%d.png' % i), frame)


if __name__ == '__main__':
  app.run(main)
