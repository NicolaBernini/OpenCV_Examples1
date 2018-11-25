
### LIB ###
"""
Converts a bytestream loaded via URLLib into an OpenCV Image 
"""
def bs2image(s): 
  #np_array = np.asarray(repr, dtype="uint8")
  np_array = np.frombuffer(s, np.uint8)
  return cv2.imdecode( np_array, cv2.IMREAD_COLOR )

"""
Dynamically Loads an Image from an URL into an in memory object for OpenCV Processing 
"""
def url2img(url): 
  # NOTE: Define a "Local Endpoint PP" Mol which provides the "Read Interface Path" Mol 
  with urllib.request.urlopen(url) as local_ep:
    bs = local_ep.read()
    return bs2image(bs)

