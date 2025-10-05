import math


class OperationService:

    @staticmethod
    def calcBoxSizeForRotation(angle, width, height) -> tuple:
        """Calculates a new size (width, height) for the object, taking into account its rotation

        Args:
            angle (float): The angle
            width (int): The object width
            height (int): The object height

        Returns:
            tuple: The tuple with new width and height
        """
        radiansAngle = math.radians(angle)

        h = height * abs(math.cos(radiansAngle)) + width * abs(math.sin(radiansAngle))
        w = width * abs(math.cos(radiansAngle)) + height * abs(math.sin(radiansAngle))

        return int(w), int(h)

    @staticmethod
    def rotatePointAroundCenter(cx, cy, x, y, angleDegress):
        angleRadians = math.radians(angleDegress)

        dx = x - cx
        dy = y - cy

        x1 = dx * math.cos(angleRadians) - dy * math.sin(angleRadians)
        y1 = dx * math.sin(angleRadians) + dy * math.cos(angleRadians)

        return (x1 + cx, y1 + cy)

    @staticmethod
    def getRotatedRectangleCoords(cx, cy, width, height, angleDegress):
        vertices = [
            (cx - width / 2, cy - height / 2),
            (cx + width / 2, cy - height / 2),
            (cx - width / 2, cy + height / 2),
            (cx + width / 2, cy + height / 2),
        ]

        rotatedVertices = [
            OperationService.rotatePointAroundCenter(cx, cy, x, y, angleDegress)
            for (x, y) in vertices
        ]

        xs, ys = zip(*rotatedVertices)
        xMin, xMax = min(xs), max(xs)
        yMin, yMax = min(ys), max(ys)

        finalX = (xMin + xMax) / 2
        finalY = (yMin + yMax) / 2

        return finalX, finalY
