#!/usr/bin/env python3
"""
Image compression script for Sigma Games carousel assets.
Uses Pillow library to compress JPEG images while maintaining quality.
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow library...")
    os.system(f"{sys.executable} -m pip install --user Pillow")
    from PIL import Image

def compress_image(image_path, quality=80, max_width=1200):
    """Compress a single image file."""
    try:
        # Get original file size
        original_size = os.path.getsize(image_path)
        
        # Create backup directory
        backup_dir = image_path.parent / 'backup'
        backup_dir.mkdir(exist_ok=True)
        backup_path = backup_dir / image_path.name
        
        # Create backup if it doesn't exist
        if not backup_path.exists():
            import shutil
            shutil.copy2(image_path, backup_path)
        
        # Open the image
        img = Image.open(image_path)
        
        # Resize if too large (while maintaining aspect ratio)
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Convert to RGB if necessary (for PNG with transparency)
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = rgb_img
        
        # Save compressed version
        img.save(image_path, 'JPEG', quality=quality, optimize=True)
        
        # Get new file size
        new_size = os.path.getsize(image_path)
        savings = ((original_size - new_size) / original_size * 100)
        
        print(f"✓ {image_path.name}: {original_size/1024:.2f}KB → {new_size/1024:.2f}KB ({savings:.2f}% reduction)")
        
        return original_size, new_size
        
    except Exception as e:
        print(f"✗ Error compressing {image_path.name}: {str(e)}")
        return 0, 0

def compress_directory(dir_path, quality=80):
    """Compress all images in a directory and its subdirectories."""
    total_original = 0
    total_compressed = 0
    file_count = 0
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(dir_path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')) and file != 'backup':
                file_path = Path(root) / file
                original, compressed = compress_image(file_path, quality)
                total_original += original
                total_compressed += compressed
                if original > 0:
                    file_count += 1
    
    return total_original, total_compressed, file_count

def main():
    # Get the script directory
    script_dir = Path(__file__).parent
    carousels_path = script_dir / 'Assets' / 'Carousels'
    
    if not carousels_path.exists():
        print(f"Error: Carousels directory not found at {carousels_path}")
        return
    
    print("=" * 60)
    print("Image Compression Script")
    print("=" * 60)
    print(f"\nCompressing images in: {carousels_path}")
    print("Settings: Quality=80%, Max Width=1200px")
    print("Creating backups in 'backup' folders\n")
    
    total_original, total_compressed, file_count = compress_directory(carousels_path, quality=80)
    
    if file_count > 0:
        total_savings = ((total_original - total_compressed) / total_original * 100)
        print("\n" + "=" * 60)
        print("✓ Compression complete!")
        print("=" * 60)
        print(f"Files compressed: {file_count}")
        print(f"Original size: {total_original/1024/1024:.2f}MB")
        print(f"Compressed size: {total_compressed/1024/1024:.2f}MB")
        print(f"Total savings: {total_savings:.2f}% ({(total_original-total_compressed)/1024/1024:.2f}MB)")
        print("\nNote: Original files are backed up in 'backup' folders within each row directory")
        print("You can delete the backup folders once you verify everything looks good.")
    else:
        print("\nNo images found to compress.")

if __name__ == "__main__":
    main()
