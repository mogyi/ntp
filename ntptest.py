import ntplib

client = ntplib.NTPClient()
for i in range(10):
	response = client.request('0.hu.pool.ntp.org', version=4)
	print str(i) + ': '
	# @property
	#     def offset(self):
	#         """offset"""
	#         return ((self.recv_timestamp - self.orig_timestamp) +
	#                 (self.tx_timestamp - self.dest_timestamp))/2

	print response.offset

	# @property
	#     def delay(self):
	#         """round-trip delay"""
	#         return ((self.dest_timestamp - self.orig_timestamp) -
	#                 (self.tx_timestamp - self.recv_timestamp))

	print response.delay