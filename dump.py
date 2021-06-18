import lldb

def processRAM():
    f = open("/Users/" + os.environ.get('USER') + "/Desktop/dump.txt", "wb")
    process = lldb.debugger.GetSelectedTarget().GetProcess()
    memoryRegions = process.GetMemoryRegions()
    memoryRegionsCount = memoryRegions.GetSize()
    memoryRegionIndex = 0
    while (memoryRegionIndex < memoryRegionsCount):
        memoryRegionInfo = lldb.SBMemoryRegionInfo()
        success = memoryRegions.GetMemoryRegionAtIndex(memoryRegionIndex, memoryRegionInfo)
        if success:
            print("Processing: "+str(memoryRegionIndex+1)+"/"+str(memoryRegionsCount))
            f.write(processRegion(process, memoryRegionInfo))
        else:
            print("Could not get memory at index: "+str(memoryRegionIndex))    
        memoryRegionIndex = memoryRegionIndex+1
    f.close()

def processRegion(process, memoryRegionInfo):
    startRAMRegion = memoryRegionInfo.GetRegionBase()
    endRAMRegion = memoryRegionInfo.GetRegionEnd()
    if memoryRegionInfo.IsReadable():
        error = lldb.SBError()
        regionSize = endRAMRegion-startRAMRegion
        data = process.ReadMemory(startRAMRegion, regionSize, error)
        if error.Success():
            return data
            pass
        else:
            print("Could not access memory data.")
    else:
        print("Memory region is not readable.")

def addressString(address):
    return '0x{:016x}'.format(address)

