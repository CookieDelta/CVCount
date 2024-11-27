import cv2
import os
import numpy as np
from camera import Camera #Camera class from camera.py
from config import Config  

class MaskApplier:
    @staticmethod
    def save_screenshot(frame, output_path="output/mask.png"):
        """
        Save a screenshot from the camera feed as a mask.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, frame)
        print(f"Mask saved at: {output_path}")

    def select_roi(self, camera_source, mask_file="output/mask.png"):
        """
        Check if mask.png exists, if not allow user to select a polygon ROI and save it as a mask.
        """
        # Check if the mask already exists
        if os.path.exists(mask_file):
            print("Mask already exists, proceeding with the mask.")
            return cv2.imread(mask_file)

        # Capture a frame from the camera
        frame = camera_source.get_frame()
        if frame is None:
            print("Failed to capture an image from the camera.")
            return None

        print("Please click to select the polygon vertices. Press 'ENTER' to finish.")
        
        # Create an empty list to store the vertices of the polygon
        points = []

        # Define mouse callback function to store points on click
        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                # Append the point to the list of vertices
                points.append((x, y))
                # Draw the point and connect it to the last one if applicable
                if len(points) > 1:
                    cv2.line(frame, points[-2], points[-1], (0, 255, 0), 2)
                cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                cv2.imshow("Select ROI", frame)

        # Set the callback function for mouse events
        cv2.imshow("Select ROI", frame)
        cv2.setMouseCallback("Select ROI", click_event)

        # Wait until the user presses 'ENTER' to finish selecting the polygon
        while True:
            cv2.imshow("Select ROI", frame)
            if cv2.waitKey(1) & 0xFF == 13:  # Press Enter to finish
                break

        # If the user has selected points, create the mask
        if len(points) > 2:
            # Convert points to a numpy array and create the polygon mask
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            pts = np.array(points, dtype=np.int32)
            cv2.fillPoly(mask, [pts], (255))
            masked_frame = cv2.bitwise_and(frame, frame, mask=mask)

            # Show the masked image with the polygon
            cv2.imshow("Masked Image", masked_frame)
            cv2.waitKey(0)

            # Ask the user if they want to save the mask
            save_mask = input("Do you want to save this mask as mask.png? (y/n): ")
            if save_mask.lower() == "y":
                self.save_screenshot(masked_frame, mask_file)
        else:
            print("Not enough points selected. Please select at least 3 points for a polygon.")

        # Release the camera and close the window
        cv2.destroyAllWindows()
        return cv2.imread(mask_file) if os.path.exists(mask_file) else None

# Test the MaskApplier class
if __name__ == "__main__":
    # Configure the source (Webcam/RTSP)
    source_type = "webcam"  # Values "webcam" or "rtsp" 
    rtsp_url = Config.RTSP_URL
    
    if source_type == "rtsp":
        camera = Camera(rtsp_url)  # Use RTSP stream
    else:
        camera = Camera(0)  # Use default webcam (0 is default)

    # Create an instance of MaskApplier and use the selected camera source
    mask_applier = MaskApplier()
    mask = mask_applier.select_roi(camera)  # Passing camera object as camera_source
    if mask is not None:
        print("Mask successfully applied.")
    else:
        print("Mask creation failed.")

    # Release the camera connection after usage
    camera.release()
