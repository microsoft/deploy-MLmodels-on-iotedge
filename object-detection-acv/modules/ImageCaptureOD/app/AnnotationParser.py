#To make python 2 and python 3 compatible code
from __future__ import absolute_import
import json

#Returns rectangle boundaries in the CV2 format (topLeftX, topLeftY, bottomRightX, bottomRightY) given by a processing service
class AnnotationParser:
    def getCV2RectanglesFromProcessingService1(self, response):
        r_dict = json.loads(response)
        preds = r_dict['predictions']
        w = 256
        h = 256
        try:
            listOfCV2Rectangles = []
            for i in range(len(preds)):
                   if(preds[i]['probability']>0.40):
                        ymin=preds[i]['boundingBox']['top']
                        xmin=preds[i]['boundingBox']['left']
                        ymax=preds[i]['boundingBox']['height']
                        xmax=preds[i]['boundingBox']['width']
                        if ymin is not None and xmin is not None and ymax is not None and xmax is not None:
                            topLeftX = xmin * w 
                            topLeftY = ymin * h
                            bottomRightX = (xmin+xmax) * w
                            bottomRightY = (ymin+ymax) * h
                            listOfCV2Rectangles.append([topLeftX, topLeftY, bottomRightX, bottomRightY])
            return listOfCV2Rectangles
        except:
            #Ignoring exceptions for now so that video can be read and analyzed without post-processing in case of errors
            pass

    def getCV2RectanglesFromProcessingService2(self, response):
            try:
                listOfCV2Rectangles = []
                for item in response:
                    for decoration in item:
                        if "rect" in decoration.lower():
                            for decorationProperty in item[decoration]:
                                if "top" in decorationProperty.lower():
                                    top = int(item[decoration][decorationProperty])
                                if "left" in decorationProperty.lower():
                                    left = int(item[decoration][decorationProperty])
                                if "width" in decorationProperty.lower():
                                    width = int(item[decoration][decorationProperty])
                                if "height" in decorationProperty.lower():
                                    height = int(item[decoration][decorationProperty])
                            if top is not None and left is not None and width is not None and height is not None:
                                topLeftX = left
                                topLeftY = top
                                bottomRightX = left + width
                                bottomRightY = top + height
                                listOfCV2Rectangles.append([topLeftX, topLeftY, bottomRightX, bottomRightY])
                return listOfCV2Rectangles
            except:
                #Ignoring exceptions for now so that video can be read and analyzed without post-processing in case of errors
                pass
    