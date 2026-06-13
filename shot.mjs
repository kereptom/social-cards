import { chromium } from 'playwright';
import fs from 'fs';
const root='/home/kerepecky/Projects/30_social_cards';
const man=JSON.parse(fs.readFileSync(root+'/build/manifest.json','utf8'));
const b=await chromium.launch();
for(const c of man){
  const pg=await b.newPage({viewport:{width:c.w,height:c.h},deviceScaleFactor:2});
  await pg.goto('file://'+root+'/templates/'+c.slug+'/index.html',{waitUntil:'networkidle',timeout:25000});
  await pg.waitForTimeout(500);
  await pg.screenshot({path:root+'/templates/'+c.slug+'/card.png'});
  await pg.close();
  console.log('rendered',c.nn,c.fmt,c.w+'x'+c.h);
}
await b.close();
