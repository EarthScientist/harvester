
# # NOTES:

# library(raster)
# library(maptools)
# library(rgdal)
# library(sp)

# out_path = "/workspace/Shared/NSIDC_Monthly/gsfc_output/converted_GTIFF/"
# files = list.files("/workspace/Shared/NSIDC_Monthly/gsfc_data", pattern=".bin$", full.names=T)

# for(f in files){

# 	print(paste("working on: ",basename(f),sep=""))
# 	pixel <- 25000 #pixel dimension in meters for both x and y 
# 	xMin <- -3850000 #From NSIDC: ulxmap -3837500 
# 	xMax <- xMin + (pixel*304) 
# 	yMax <- 5850000 #From NSIDC: ulymap 5837500 
# 	yMin <- yMax - (pixel*448) 
# 	rr <- raster(nrow=448, ncol=304, xmn=xMin, xmx=xMax, ymn=yMin, ymx=yMax) 
# 	# rr <- raster(matrix(bin,nrow=448,ncol=304,byrow=TRUE),xmn=-3850,xmx=3750,ymn=-5350,ymx=5850)
# 	projection(rr) <- "+proj=stere +lat_0=90 +lat_ts=70 +lon_0=-45 +k=1 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs +ellps=WGS84 +towgs84=0,0,0" #'+proj=stere +lat_0=90 +lat_ts=70 +lon_0=-45 +k=1 +x_0=0 +y_0=0 +a=6378273 +b=6356889.449 +units=m +no_defs' 

# 	bin <- file(f,"rb")
# 	read.bin <- readBin(bin, what="integer", n=136192, size=2, signed=FALSE, endian="little")
# 	rr <- setValues(rr, (read.bin/10))

# 	writeRaster(rr, filename=paste(out_path,extension(basename(f),".tif"),sep=""), options="COMPRESS=LZW")
# }

# # to get the xmin ymax values, I have taken the WGS1984 tie points from the NSIDC site and projected them into a NSIDC Arctic Polar WGS1984 projection system
# # then used those values to recreate the projected bounding box


import urllib2, os

path = 'ftp://sidads.colorado.edu/pub/DATASETS/nsidc0051_gsfc_nasateam_seaice/final-gsfc/north/monthly'

# urrlib approach attempt
req = urllib2.Request( path )

response = urllib2.urlopen( req )

filelist = response.read()
filelist = filelist.splitlines()[1:] # remove file count which is first line

# filenames = [ os.path.splitext( f.split()[len(f.split())-1] )[0] for f in filelist ]

def get_date( f ):
	fn = f.split()[len(f.split())-1]
	split = fn.split( "_" )
	w,date,_,_,_ = split
	return( fn, date )

splitter =[ get_date( f ) for f in filelist ]


[ urllib.urlretreive(os.path.join( path, i )) for i,j in filelist ]


# numpy.fromfile(f, dtype=np.int8)
