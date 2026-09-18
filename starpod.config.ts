/**
 * starpod.config.ts
 * Starpod Podcast Engine Configuration for Ngesa Diaries
 * Host: Dominic Nyongesa (@ngesa-cloud)
 */

export interface StarpodConfig {
  title: string;
  description: string;
  author: string;
  audioBaseUrl: string;
  preloadNextEpisodeSeconds: number;
  episodesManifest: string;
  rssPath: string;
  theme: {
    mode: 'dark' | 'light';
    accentColor: string;
    dangerColor: string;
    fontFamily: string;
  };
  audioPipeline: {
    targetLufs: number;
    truePeakLimitDbfs: number;
    highpassCutoffHz: number;
    voiceSource: 'actor' | 'dataset' | 'synthetic';
  };
}

export const config: StarpodConfig = {
  title: 'Ngesa Diaries — Hidden Kenyan Horror Stories & True Mysteries',
  description: 'An open-source investigative audio documentary series exploring declassified Kenyan horror folklore, urban legends, and supernatural mysteries.',
  author: 'Dominic Nyongesa',
  
  // Starpod Audio Settings
  audioBaseUrl: '/audio',
  preloadNextEpisodeSeconds: 10,
  episodesManifest: './audio/manifest.json',
  rssPath: './podcast.xml',

  theme: {
    mode: 'dark',
    accentColor: '#d9a441', // Ochre Gold
    dangerColor: '#ff3355', // Rift Valley Crimson
    fontFamily: 'Newsreader, Georgia, serif'
  },

  audioPipeline: {
    targetLufs: -16.0,
    truePeakLimitDbfs: -1.5,
    highpassCutoffHz: 80,
    voiceSource: 'actor'
  }
};

export default config;
