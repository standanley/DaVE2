def test_magma():
    import magma
    print(magma)

def test_fault():
    import fault
    print(fault)

def test_verilator():
    import magma as m
    import fault

    class MyBuff(m.Circuit):
        name = 'my_inv'
        IO = ['in_', m.BitIn, 'out', m.BitOut]
        @classmethod
        def definition(io):
            io.out <= io.in_

    tester = fault.Tester(MyBuff)

    tester.poke(MyBuff.in_, 0)
    tester.eval()
    tester.expect(MyBuff.out, 0)
    tester.poke(MyBuff.in_, 1)
    tester.eval()
    tester.expect(MyBuff.out, 1)

    tester.compile_and_run('verilator', flags=['-Wno-fatal'])
