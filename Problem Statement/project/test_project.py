from project import gain_transaction, loss_transaction, display_transaction

def test_gain_transaction():
    assert gain_transaction(100,200) == 100
    assert gain_transaction(50,100) == 50
    assert gain_transaction(0,100) == 0


def test_loss_transaction():
    assert loss_transaction(20) == -20
    assert loss_transaction(100) == -100


def test_display_transaction():
    assert display_transaction() == ['Category | Note | Amount\n','Job | Salary | +1000\n','Stationary | Pen | -20\n']
