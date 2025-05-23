import rclpy
from rclpy.node import Node
from synapse_msgs.msg import TrafficStatus

import cv2
import numpy as np

from sensor_msgs.msg import CompressedImage

QOS_PROFILE_DEFAULT = 10


class ObjectRecognizer(Node):
	""" Initializes object recognizer node with the required publishers and subscriptions.

		Returns:
			None
	"""
	def __init__(self):
		super().__init__('object_recognizer')

		# Subscription for camera images.
		self.subscription_camera = self.create_subscription(
			CompressedImage,
			'/camera/image_raw/compressed',
			self.camera_image_callback,
			QOS_PROFILE_DEFAULT)

		# Publisher for traffic status.
		self.publisher_traffic = self.create_publisher(
			TrafficStatus,
			'/traffic_status',
			QOS_PROFILE_DEFAULT)

	""" Analyzes the image received from /camera/image_raw/compressed to detect traffic signs.
		Publishes the existence of traffic signs in the image on the /traffic_status topic.
		Also, displays the camera image using OpenCV.

		Args:
			message: "docs.ros.org/en/melodic/api/sensor_msgs/html/msg/CompressedImage.html"

		Returns:
			None
	"""
	def camera_image_callback(self, message):
		# Convert message to an n-dimensional numpy array representation of image.
		np_arr = np.frombuffer(message.data, np.uint8)
		image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

		# Display the camera image.
		cv2.imshow("Camera Feed", image)
		cv2.waitKey(1)  # Necessary for OpenCV window updates

		traffic_status_message = TrafficStatus()

		# NOTE: Participants need to implement logic for recognizing traffic signs.

		self.publisher_traffic.publish(traffic_status_message)


def main(args=None):
	rclpy.init(args=args)

	object_recognizer = ObjectRecognizer()

	rclpy.spin(object_recognizer)

	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	object_recognizer.destroy_node()
	rclpy.shutdown()

	# Close OpenCV windows
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()

