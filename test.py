import unittest
import main as scapy_main

class TestScapyMain(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.packet = scapy_main.packet_sniffer()
	
	def setUp(self) -> None:
		print("\n{} \nSet up".format(self.id().split('.')[-1]))

	def tearDown(self) -> None:
		print("Tearing down")


	def test_PacketSniffer(self):
		if self.packet  is None:
			self.assertEqual(isinstance(self.packet , type(None)), True)
		else:
			self.assertEqual(isinstance(self.packet , dict), True)


	def test_PacketDecoding(self):
		if self.packet  is None:
			self.assertEqual(isinstance(self.packet , type(None)), True)
		else:
			self.assertEqual(isinstance(scapy_main.packet_decoding(self.packet .get('ActualPayload')), str), True)

	def test_PacketManipulation(self):
		data = ['127.0.0.1', '127.0.0.1', 8080, 8081, 'hello']
		self.assertEqual(scapy_main.packet_manipulation(data), True)
		

if __name__ == "__main__":
	unittest.main()
