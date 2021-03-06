import numpy as np
import mahotas.tas
def test_tas():
    np.random.seed(22)
    f = np.random.rand(1024, 1024)
    f = (f * 255).astype(np.uint8)
    assert np.abs(mahotas.tas.tas(f).sum()-6) < 0.0001
    assert np.abs(mahotas.tas.pftas(f).sum()-6) < 0.0001

def test_tas3d():
    np.random.seed(22)
    f = np.random.rand(512, 512, 8)
    f = (f * 255).astype(np.uint8)
    assert np.abs(mahotas.tas.tas(f).sum()-6) < 0.0001
    assert np.abs(mahotas.tas.pftas(f).sum()-6) < 0.0001

def test_regression():
    np.random.seed(220)
    img = np.random.random_sample((1024,1024))
    img *= 255
    img = img.astype(np.uint8)
    features = mahotas.tas.pftas(img)
    assert not np.any(features == 0.)

def test_zero_image():
    features = mahotas.tas.pftas(np.zeros((64,64), np.uint8))
    assert not np.any(np.isnan(features))
