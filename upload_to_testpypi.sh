#!/bin/bash
# Upload hfortix to TestPyPI and verify
#
# Usage: ./upload_to_testpypi.sh [version]
# Example: ./upload_to_testpypi.sh 0.3.33.dev5

set -e  # Exit on error

VERSION="${1:-0.3.33.dev5}"

# Load TestPyPI token from .env file
if [ -f "X/.env" ]; then
    export $(grep -v '^#' X/.env | grep TESTPYPI_TOKEN | xargs)
fi

echo "======================================================================"
echo "Uploading hfortix version $VERSION to TestPyPI"
echo "======================================================================"

# Check if twine is installed
if ! command -v twine &> /dev/null; then
    echo "Error: twine not found. Install with: pip install twine"
    exit 1
fi

# Check if build is installed
if ! python -m build --help &> /dev/null; then
    echo "Error: build not found. Install with: pip install build"
    exit 1
fi

# 1. Clean previous builds
echo ""
echo "Step 1: Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info hfortix.egg-info/

# 2. Build the package
echo ""
echo "Step 2: Building package..."
python -m build

# 3. Check the build
echo ""
echo "Step 3: Listing built files..."
ls -lh dist/

# 4. Upload to TestPyPI
echo ""
echo "Step 4: Uploading to TestPyPI..."

# Check if token is set
if [ -n "$TESTPYPI_TOKEN" ]; then
    echo "Using token from X/.env file..."
    python -m twine upload --repository testpypi dist/* --username __token__ --password "$TESTPYPI_TOKEN"
else
    echo "NOTE: You'll need to enter your TestPyPI API token"
    echo "      (To avoid this prompt, add TESTPYPI_TOKEN to X/.env)"
    python -m twine upload --repository testpypi dist/*
fi

# 5. Show success message
echo ""
echo "======================================================================"
echo "✓ Upload successful!"
echo "======================================================================"
echo ""
echo "View your package at:"
echo "https://test.pypi.org/project/hfortix/$VERSION/"
echo ""
echo "To install on another system:"
echo "  pip install --index-url https://test.pypi.org/simple/ \\"
echo "              --extra-index-url https://pypi.org/simple/ \\"
echo "              hfortix==$VERSION"
echo ""
echo "To test locally:"
echo "  python -m venv test-env"
echo "  source test-env/bin/activate"
echo "  pip install --index-url https://test.pypi.org/simple/ \\"
echo "              --extra-index-url https://pypi.org/simple/ \\"
echo "              hfortix==$VERSION"
echo "  python -c 'import hfortix; print(hfortix.__version__)'"
echo "  deactivate"
echo "  rm -rf test-env"
echo ""
