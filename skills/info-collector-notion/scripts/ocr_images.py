#!/usr/bin/env python3
"""
OCR extract text from images using rapidocr-onnxruntime.
Designed for XHS image notes where article content is embedded in images.

Usage:
    python ocr_images.py <images_dir> [--output <output_file>]

Example:
    python ocr_images.py "C:\\path\\to\\images"
    python ocr_images.py "C:\\path\\to\\images" --output "output.txt"
"""
import os, sys, glob, argparse


def ocr_images(images_dir, output_file=None):
    images = sorted(glob.glob(os.path.join(images_dir, "img_*.jpg")))
    if not images:
        # Try any image format
        images = sorted(
            glob.glob(os.path.join(images_dir, "*.jpg"))
            + glob.glob(os.path.join(images_dir, "*.png"))
            + glob.glob(os.path.join(images_dir, "*.jpeg"))
        )

    if not images:
        print(f"No images found in {images_dir}", file=sys.stderr)
        return ""

    print(f"Found {len(images)} images", flush=True)

    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        print(
            "rapidocr-onnxruntime not installed. Install with:\n"
            '  pip install rapidocr-onnxruntime',
            file=sys.stderr,
        )
        sys.exit(1)

    engine = RapidOCR()
    all_text = []

    for img_path in images:
        fname = os.path.basename(img_path)
        print(f"Processing {fname}...", flush=True)
        result, elapse = engine(img_path)
        if result:
            texts = [item[1] for item in result]
            text = "\n".join(texts)
            all_text.append(text)
            print(f"  Got {len(texts)} text blocks, {len(text)} chars", flush=True)
        else:
            print(f"  No text detected", flush=True)

    full_text = "\n\n".join(all_text)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"\nOutput saved to {output_file}")

    print(f"Total text length: {len(full_text)} chars")
    print("\n=== FULL TEXT ===")
    print(full_text)

    return full_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OCR extract text from images")
    parser.add_argument("images_dir", help="Directory containing images")
    parser.add_argument("--output", "-o", help="Output file path (optional)")
    args = parser.parse_args()

    ocr_images(args.images_dir, args.output)
