import { Button, Select, Switch } from "@chakra-ui/react";
import SubSectionLayout from "../../../components/layouts/subsection_layout"
import ConfigRow from "../../../components/data/config_row";


function VideoTab() {
    return (
        <div className="flex flex-col items-start p-4 space-y-2">
            <SubSectionLayout title={"Main Stream"}>
                <ConfigRow title="Smart codec" component={
                    <Switch />
                } />
                <ConfigRow title="Type" component={
                    <Select >
                        <option>General</option>
                    </Select>
                } />
                <ConfigRow title="Compression" component={
                    <Select >
                        <option>General</option>
                    </Select>
                } />
                <ConfigRow title="Resolution" component={
                    <Select >
                        <option>1920x1080 (4MP)</option>
                    </Select>
                } />
                <ConfigRow title="Frame rate (FPS)" component={
                    <Select >
                        <option>30</option>
                    </Select>
                } />
                <ConfigRow title="Bit rate type" component={
                    <Select >
                        <option>CBR</option>
                    </Select>
                } />
                <ConfigRow title="Quality" component={
                    <Select >
                        <option>4</option>
                    </Select>
                } />
                <ConfigRow title="Bit rate (Kb/s)" component={
                    <Select >
                        <option>1024</option>
                    </Select>
                } />

            </SubSectionLayout>
            <SubSectionLayout title={"Sub Stream"}>
                <ConfigRow title="Smart codec" component={
                    <Switch />
                } />
                <ConfigRow title="Type" component={
                    <Select >
                        <option>General</option>
                    </Select>
                } />
                <ConfigRow title="Compression" component={
                    <Select >
                        <option>General</option>
                    </Select>
                } />
                <ConfigRow title="Resolution" component={
                    <Select >
                        <option>1920x1080 (4MP)</option>
                    </Select>
                } />
                <ConfigRow title="Frame rate (FPS)" component={
                    <Select >
                        <option>30</option>
                    </Select>
                } />
                <ConfigRow title="Bit rate type" component={
                    <Select >
                        <option>CBR</option>
                    </Select>
                } />
                <ConfigRow title="Quality" component={
                    <Select >
                        <option>4</option>
                    </Select>
                } />
                <ConfigRow title="Bit rate (Kb/s)" component={
                    <Select >
                        <option>1024</option>
                    </Select>
                } />

            </SubSectionLayout>
            <div className="flex flex-row justify-start space-x-2">
                <Button colorScheme="blue" paddingTop={1}>Save changes</Button>
                <Button colorScheme="gray" paddingTop={1}>Cancel</Button>
            </div>
        </div>
    )
}

export default VideoTab