import { Tabs, TabList, Tab, TabPanels, TabPanel } from "@chakra-ui/react";
import PageTitle from "../../components/headings/PageTitle";
import ContentLayout from "../../components/layouts/content_layout";
import settingTabs from "./tabs/tabs";
import React from "react";
import { IconType, IconBaseProps } from "react-icons";

function SettingPage() {
    return (
        <ContentLayout>
            <PageTitle>Settings</PageTitle>
            <div className="flex flex-row w-full">
                <Tabs className="w-full bg-white rounded-lg" variant='enclosed'>
                    <TabList>
                        {settingTabs.map((tab) =>
                            <Tab className="flex items-center space-x-1" key={tab.title}>
                                {React.cloneElement<IconBaseProps>(tab.icon, { size: 24 })}
                                <span className="pt-1">{tab.title}</span>
                            </Tab>)}
                    </TabList>
                    <TabPanels>
                        {settingTabs.map((tab) => <TabPanel key={tab.title}>{tab.component}</TabPanel>)}

                    </TabPanels>
                </Tabs>

            </div>
        </ContentLayout>
    )
}

export default SettingPage;