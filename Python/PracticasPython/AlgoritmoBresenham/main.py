import cv2
import numpy as np

def bresenham(img : list, x1 : int, y1 : int, x2 : int, y2 : int, color = 255) -> None:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    
    if dx > dy:
        err = dx / 2.0
        
        while x != x2:
            img[y, x] = color
            
            err -= dy
            
            if err < 0:
                y += sy
                err += dx
            
            x += sx
    else:
        err = dy / 2.0
        
        while y != y2:
            img[y, x] = color
            
            err -= dx
            
            if err < 0:
                x += sx
                err += dy
            
            y += sy
    
    img[y, x] = color

def main():
    WIDTH, HEIGHT = 400, 400
    BACKGROUND_COLOR = (255, 255, 255)
    LINE_COLOR = (0, 0, 255)
    
    img = np.full((HEIGHT, WIDTH, 3), BACKGROUND_COLOR, dtype = np.uint8)
    
    x1, y1 = [int(input('Enter x1: ')), int(input('Enter y1: '))]
    x2, y2 = [int(input('Enter x2: ')), int(input('Enter y2: '))]
    
    bresenham(img, x1, y1, x2, y2, color = LINE_COLOR)
    
    cv2.imshow('Bresenham Algorithm', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
