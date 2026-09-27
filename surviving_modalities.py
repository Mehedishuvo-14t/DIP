import cv2
import matplotlib.pyplot as plt

images = {
    'X-Ray': ('xray.jpg', 'X-ray imaging is widely used in medicine for detecting bone fractures and dental issues.'),
    'Satellite': ('satellite.jpg', 'Remote sensing image analysis is critical for environmental monitoring and agricultural planning.'),
    'Microscopy': ('microscopy.jpg', 'Microscopy imaging enables detailed biological analysis at cellular and subcellular scales.'),
    'Ultrasound': ('ultrasound.jpg', 'Ultrasound imaging provides real-time visualization of internal organs and fetal development.'),
    'Infrared': ('infrared.jpg', 'Thermal infrared imaging is essential for industrial defect detection and building insulation inspection.')
}

plt.figure(figsize=(15, 6))

for index, (modality, (path, sentence)) in enumerate(images.items(), 1):
    img = cv2.imread(path)
    if img is not None:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(1, 5, index)
        plt.imshow(img_rgb)
        plt.title(f"{modality}\n\n{sentence}", fontsize=8)
        plt.axis("off")

plt.tight_layout()
plt.show()