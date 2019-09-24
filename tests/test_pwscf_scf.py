import os
import numpy as np
import unittest
from context import dpdata

class TestPWSCFSinglePointEnergy:

    def test_atom_names(self) :
        self.assertEqual(self.system_ch4.data['atom_names'], ['H','C'])
        self.assertEqual(self.system_h2o.data['atom_names'], ['O','H'])

    def test_atom_numbs(self) :
        self.assertEqual(self.system_ch4.data['atom_numbs'], [4,1])
        self.assertEqual(self.system_h2o.data['atom_numbs'], [64,128])

    def test_atom_types(self) :
        ref_type = [0,0,0,0,1]
        ref_type =  np.array(ref_type)
        for ii in range(ref_type.shape[0]) :
            self.assertEqual(self.system_ch4.data['atom_types'][ii], ref_type[ii])

        ref_type = [0]*64 + [1]*128
        ref_type =  np.array(ref_type)
        for ii in range(ref_type.shape[0]) :
            self.assertEqual(self.system_h2o.data['atom_types'][ii], ref_type[ii])

    def test_cell(self) :
        cell = 10 * np.eye(3)
        for ii in range(cell.shape[0]) :
            for jj in range(cell.shape[1]) :
                self.assertEqual(self.system_ch4.data['cells'][0][ii][jj], cell[ii][jj])

        fp = open('pwscf.scf/h2o_cell')
        cell = []
        for ii in fp :
            cell.append([float(jj) for jj in ii.split()])
        cell = np.array(cell)
        for ii in range(cell.shape[0]) :
            for jj in range(cell.shape[1]) :
                self.assertEqual(self.system_h2o.data['cells'][0][ii][jj], cell[ii][jj])


    def test_coord(self) :
        fp = open('pwscf.scf/ch4_coord')
        coord = []
        for ii in fp :
            coord.append([float(jj) for jj in ii.split()])
        coord = np.array(coord)
        for ii in range(coord.shape[0]) :
            for jj in range(coord.shape[1]) :
                self.assertEqual(self.system_ch4.data['coords'][0][ii][jj], coord[ii][jj])
        fp.close()

        fp = open('pwscf.scf/h2o_coord')
        coord = []
        for ii in fp :
            coord.append([float(jj) for jj in ii.split()])
        coord = np.array(coord)
        for ii in range(coord.shape[0]) :
            for jj in range(coord.shape[1]) :
                self.assertEqual(self.system_h2o.data['coords'][0][ii][jj], coord[ii][jj])
        fp.close()

    def test_force(self) :
        fp = open('pwscf.scf/ch4_force')
        force = []
        for ii in fp :
            force.append([float(jj) for jj in ii.split()])
        force = np.array(force)
        for ii in range(force.shape[0]) :
            for jj in range(force.shape[1]) :
                self.assertEqual(self.system_ch4.data['forces'][0][ii][jj], force[ii][jj])
        fp.close()

        fp = open('pwscf.scf/h2o_force')
        force = []
        for ii in fp :
            force.append([float(jj) for jj in ii.split()])
        force = np.array(force)
        for ii in range(force.shape[0]) :
            for jj in range(force.shape[1]) :
                self.assertEqual(self.system_h2o.data['forces'][0][ii][jj], force[ii][jj])
        fp.close()

    def test_virial(self) :
        fp = open('pwscf.scf/ch4_virial')
        virial = []
        for ii in fp :
            virial.append([float(jj) for jj in ii.split()])
        virial = np.array(virial)
        for ii in range(virial.shape[0]) :
            for jj in range(virial.shape[1]) :
                self.assertEqual(self.system_ch4.data['virials'][0][ii][jj], virial[ii][jj])
        fp.close()

        fp = open('pwscf.scf/h2o_virial')
        virial = []
        for ii in fp :
            virial.append([float(jj) for jj in ii.split()])
        virial = np.array(virial)
        for ii in range(virial.shape[0]) :
            for jj in range(virial.shape[1]) :
                self.assertEqual(self.system_h2o.data['virials'][0][ii][jj], virial[ii][jj])
        fp.close()

    def test_energy(self) :
        ref_energy = -219.74425946528794
        self.assertEqual(self.system_ch4.data['energies'][0], ref_energy)
        ref_energy = -30007.651851226798
        self.assertEqual(self.system_h2o.data['energies'][0], ref_energy)



class TestPWSCFLabeledOutput(unittest.TestCase, TestPWSCFSinglePointEnergy):

    def setUp(self):
        self.system_ch4 = dpdata.LabeledSystem('pwscf.scf/01.out',fmt='pwscf/scf')
        self.system_h2o = dpdata.LabeledSystem('pwscf.scf/02.out',fmt='pwscf/scf')

class TestPWSCFLabeledOutputListInput(unittest.TestCase, TestPWSCFSinglePointEnergy):

    def setUp(self):
        self.system_ch4 = dpdata.LabeledSystem(['pwscf.scf/01.in', 'pwscf.scf/01.out'], fmt='pwscf/scf')
        self.system_h2o = dpdata.LabeledSystem(['pwscf.scf/02.in', 'pwscf.scf/02.out'], fmt='pwscf/scf')


if __name__ == '__main__':
    unittest.main()
