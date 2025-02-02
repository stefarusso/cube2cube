def main():
    """
    take gdma.grid produced by potential 1 thinker package
    and grid_esp.dat produced by esp.psi4 to produce the 
    correct thinker cube format (different from gaussian 
    cube)
    """     
    espname=str(input('ESP grid filename [grid_esp.dat]: ').strip() or "grid_esp.dat")
    gridname=str(input('grid coordinates filename [grid.dat]: ').strip() or "grid.dat")
    cubename=str(input('output filename [cubefile.cube]: ').strip() or "cubefile.cube")
    espmethod=str(input('ESP method [MP2]: ').strip() or "MP2")
    espbasisset=str(input('ESP basis set [aug-cc-pVTZ]: ').strip() or "aug-cc-pVTZ")

    temp=open(espname,'r')
    results=temp.readlines()
    temp.close()
    Vvals=[]    
    for line in results:
        linesplit=line.split()
        if len(linesplit)!=0:
            Vvals.append(linesplit[0])
                
    with open(gridname, 'r') as fp:
        gridpts = fp.readlines()
    
    with open(cubename, 'w') as fp:
        fp.write(" %s/%s potential calculation\n\n" % (espmethod,espbasisset))
        fp.write("%5d\n%5d\n\n\n" % (0,len(Vvals)))
        for xyz,v in zip(gridpts, Vvals):
            fp.write("%s %s\n" % (xyz.rstrip(), v))
    return 1

main()
