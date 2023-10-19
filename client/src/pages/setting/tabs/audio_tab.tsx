import { Button, Checkbox, Select } from "@chakra-ui/react"
import ConfigRow from "../../../components/data/config_row"
import { BiSolidSave } from 'react-icons/bi'

function AudioTab() {
    return (
        <div className="flex flex-col items-start p-4 space-y-2">
            <div className="flex flex-col items-start border-[1px] border-black w-full p-4 space-y-2">
                <ConfigRow title="Record Audio" component={<Checkbox />} />

                <ConfigRow title="Audio encoding" component={
                    <Select>
                        <option>G.722</option>
                    </Select>
                } />

                <ConfigRow title="Compression" component={
                    <Select>
                        <option>H.265</option>
                    </Select>
                } />
                <ConfigRow title="Noise Filter" component={
                    <Select>
                        <option>Off</option>
                    </Select>
                } />
            </div>
            <Button className="flex justify-center items-center space-x-2" paddingTop={1} colorScheme="blue">
                <BiSolidSave />
                <span className="pt-[2px]">Save</span>
            </Button>
        </div>
    )
}

export default AudioTab